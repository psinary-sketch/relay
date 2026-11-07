"""standing/hook.py -- the PreToolUse hook of standing clauses v5 row (77), the standing toolset's copy.

Copied from tools/b714_hook.py (provenance), its act constants removed: the act is read at run time from data/act_current.json.
Installed in the seat's project settings (D:/.claude/settings.json) on the matcher Read|Bash|PowerShell.
Reads the hook's JSON from stdin and refuses, each refusal printed with the v5 row it enforces:
  READ   a Read call with no limit, or a limit above 200            -- rows (77) and (19)
  PIPE   a Bash or PowerShell command carrying a pipe outside quotes   -- rows (77) and (14)
  REDIR  a Bash or PowerShell command carrying a redirect outside quotes -- rows (77) and (14)
  ENV    a command prefixed by an environment-variable assignment     -- rows (77) and (20)
  REMOTE a Bash or PowerShell command carrying more than one ls-remote outside quotes -- row (77), (R338)(2)(iv)(d)
  POSTSEAL a shell command the arm G-RULE-POSTSEAL-READ would count, the seal recorded -- v1.13.0, (R343)(2)(vi); the arm's own lists read from tools/rule_arms.py at the call
  INPLACE a shell command editing a file in place (sed or perl -i, Set-Content) -- row (18), v1.18.0, (R348)(2)(iii)
  GITWRITE a second git write in one message, any repository, kernel clones included -- row (12); v1.19.0, (R349)(2)(i): the message
         read by its API request (the transcript's last api-request line, written before the message's tools run), a per-session
         ledger in the temporary directory, where v1.17.0's sibling read found no block (the call's own block not yet written)
  SUBJECT a seal or lock commit whose subject tools/standing/subjects.py check() faults -- v1.19.0, (R349)(2)(iii)
  BACKGROUND a suite part or combine sent with run_in_background -- v1.19.0, (R349)(2)(v), the standing clauses' foreground rule
  SED    sed in any form (data/b685_rules.txt row (2)), the reader of (R343)'s tools in its place -- v1.19.0, (R349)(2)(vi)
  HASHED an Edit or Write of a bank its tool wrote (data/<act>_bank_hashes.json names it), before the lock or after -- v1.21.0, (R351)(2)(ii)
  SUBJECT (v1.21.0, (R351)(2)(i)) a gate, lock or seal commit made by the shell at all: tools/standing/commit.py is the one route
  SUBJECT (v1.25.0, (R355)(2)(v)) a step-row commit whose subject names other rows than the staged step bank adds
  ROWID  (v1.25.0, (R355)(2)(i)) a PLACE-papers commit adding a ledger row whose ID the file already holds (tools/standing/rowid.py)
Quoted strings (single, double, PowerShell here-strings) are stripped before the scan, so a regex
argument such as "a|b" is not read as a pipe.

THE CLASS REPAIR (4)(iii) of the toolset act (provenance: the b714 hook appended to a bank its act's root names, so a refusal after the
root changed a rooted bank): each refusal is appended to data/<act>_hook_refusals.txt, <act> read from data/act_current.json at the
call, a bank of the excluded kind `hook_refusals` the root route takes out. Allowed calls print nothing and write nothing.

  python -I -X utf8 tools/standing/hook.py            the hook (stdin JSON)
  python -I -X utf8 tools/standing/hook.py control    the offline control: the judge's cases, and the (4)(iii) two instances in a scratch
                                                      directory outside data/ and tools/, bank data/<act>_hook_control.txt
"""
import ast
import datetime
import hashlib
import json
import os
import re
import sys
import tempfile

RELAY = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LIMIT = 200
EXCLUDED_KIND = 'hook_refusals'   # the kind the root route excludes (the act's record tool lists it in its EXCLUDE_KINDS)

ROW77 = ('(77) THE STANDING ROWS ENFORCED BY THE HARNESS: a PreToolUse hook in the seat’s project '
         'settings refusing a Read call with no limit or a limit above 200, a shell command carrying a pipe or a '
         'redirect, and a command prefixed by an environment variable, each refusal printed with the row it enforces')
ROWS = {
    'READ': ROW77 + ' ; (19) files read through the Read tool, whole where under two hundred lines and by '
                    'offset and a limit of at most two hundred otherwise',
    'PIPE': ROW77 + ' ; (14) no redirect of any stream and no pipe in any command, scratch, listings and '
                    'diagnostics included',
    'REDIR': ROW77 + ' ; (14) no redirect of any stream and no pipe in any command, scratch, listings and '
                     'diagnostics included',
    'ENV': ROW77 + ' ; (20) environment variables left as they are',
    'REMOTE': ROW77 + ' ; (R338)(2)(iv)(d) one remote read per command, b674 row 1',
    'SUITE': ROW77 + ' ; one suite part or combine per call, each its own message',
    'ORDER': ROW77 + ' ; the suite`s G-BRANCHES-BANKED clause, the citation check before the first delete',
    'POSTSEAL': ROW77 + ' ; the suite`s G-RULE-POSTSEAL-READ, after the seal no shell filter or redirect over the entry or the trail, its list read from tools/rule_arms.py',
    'GITWRITE': ROW77 + ' ; (12) one git write per message across every repository, add and commit counted as two, across parallel calls ((R347)(2)(ii))',
    'LOCKED': ROW77 + ' ; (65) a bank written before the lock refuses to be rewritten after it, refused before it lands ((R347)(2)(iii))',
    'INPLACE': ROW77 + ' ; (18) every file the seat writes written by the Edit or Write tool, a rendered file by its render re-run ((R348)(2)(iii))',
    'SUBJECT': ROW77 + ' ; a seal or lock commit`s subject composed from its bank by tools/standing/subjects.py ((R349)(2)(iii))',
    'BACKGROUND': ROW77 + ' ; no suite part in the background, each in the foreground with its 600 s limit ((R349)(2)(v))',
    'SED': ROW77 + ' ; data/b685_rules.txt row (2), sed in any form, a line read by the Read tool or tools/standing/peek.py ((R349)(2)(vi))',
    'HASHED': ROW77 + ' ; (18) a bank a tool wrote (named in data/<act>_bank_hashes.json) rewritten by its tool and never by hand ((R351)(2)(ii))',
    'ROWID': ROW77 + ' ; a ledger row`s ID allocated from the file`s maximum over every table carrying the prefix, a held ID refused ((R355)(2)(i))',
}

# ### v1.17.0, (R347)(2)(ii)-(iii): the hook reads the message a call belongs to, and judges the Edit and Write tools against the lock
EDIT_TOOLS = ('Edit', 'Write', 'NotebookEdit')
TAIL_BYTES = 4 * 1024 * 1024

SUITE_RUN = r'(?:_checks\.py\b|\bstanding/fold\.py\s+checks\b)'   # ### v1.11.0: tools/rule_arms.py :155-:157's two calls
SUITE_PART = re.compile(SUITE_RUN + r'[^|;&]*?--part\s+(\S+)')
SUITE_COMBINE = re.compile(SUITE_RUN + r'[^|;&]*--combine')
BRANCH_DEL = re.compile(r'\bbranch\s+(?:-[dD]|--delete)(?![\w-])')
# ### v1.18.0, (R348)(2)(iii): sed or perl with an in-place flag (-i, -i.bak, -pi, --in-place) and the PowerShell cmdlets that rewrite a file
INPLACE = re.compile(r'(?<![\w-])(?i:sed|perl)(?:\.exe)?\s(?:[^;&\n]*?\s)?(?:-[a-hj-zA-Z]*i[a-zA-Z]*(?:\.\S*)?|--in-place\S*)(?=\s|$)'
                     r'|(?<![\w-])(?i:Set-Content|Add-Content|Clear-Content)(?![\w-])')
# ### v1.19.0, (R349)(2)(vi): sed as a command word in any form, quoted text blanked first (a grep for the words passes)
SED = re.compile(r'(?<![\w./\\-])(?i:sed)(?:\.exe)?(?=\s|$)')
# ### v1.19.0, (R349)(2)(iii): a commit's first -m subject naming the seal or lock phase
COMMIT_SUBJECT = re.compile(r'\bgit\s+(?:-C\s+\S+\s+)*commit\b[^\n]*?\s-m\s+(?:"((?:[^"\\]|\\.)*)"|\'([^\']*)\')')
ASSIGN = re.compile(r'^\s*(?:env\s+)?[A-Za-z_][A-Za-z0-9_]*=')
PS_ENV = re.compile(r'(?i)^\s*\$env:[A-Za-z_][A-Za-z0-9_]*\s*=')


def act_of(relay=RELAY):
    """the act named by <relay>/data/act_current.json, or None where the file is absent or unreadable."""
    try:
        with open(os.path.join(relay, 'data', 'act_current.json'), encoding='utf-8') as f:
            return json.load(f).get('act')
    except (OSError, ValueError):
        return None


def next_of(relay=RELAY):
    """the act data/act_current.json names as next, or None."""
    try:
        with open(os.path.join(relay, 'data', 'act_current.json'), encoding='utf-8') as f:
            return json.load(f).get('next')
    except (OSError, ValueError):
        return None


def bank_act(relay=RELAY):
    """v1.10.0, (R340)(2)(iv): the one act whose refusal bank a refusal may reach: the act data/act_current.json names, while that act is open. A closed
    act (its closing bank written) has no bank left to append to: the refusal is the next act's, b729's two rows at step zero into b728's bank the case."""
    act = act_of(relay)
    if act and os.path.exists(os.path.join(relay, 'data', '%s_closing.txt' % act)):
        return next_of(relay)
    return act


def citation_done(relay=RELAY):
    """v1.11.0: the act's citation check has run: its bank's json stands. v1.18.0, (R348)(2)(iv), b737 (d): and it ran CLEAN -- its json's `clean`
    True (no halt: no differing Lean path or noun, no comparative sentence CONTRADICTS or UNREAD); a halted check's json stood before and let a delete by."""
    act = bank_act(relay)
    p = os.path.join(relay, 'data', '%s_citation_check.json' % act) if act else ''
    if not (act and os.path.exists(p)):
        return False
    try:
        with open(p, encoding='utf-8') as f:
            return json.load(f).get('clean') is True
    except (OSError, ValueError):
        return False


def sealed(relay=RELAY):
    """v1.13.0: the open act's seal is recorded: its data/<act>_seal_hashes.json stands (written just before the seal commit the arm dates from)."""
    act = bank_act(relay)
    return bool(act) and os.path.exists(os.path.join(relay, 'data', '%s_seal_hashes.json' % act))


def ledger_rule(relay=RELAY):
    """v1.13.0, (R343)(2)(vi): the post-seal read rule AS THE ARM HOLDS IT, read from tools/rule_arms.py at the call and not kept here: the ledger names, the shell filter,
    the quoted-span form, and the exclude list out of the arm's own block; None where the file does not read so (the suite's arm still stands behind the hook)."""
    try:
        with open(os.path.join(relay, 'tools', 'rule_arms.py'), encoding='utf-8') as f:
            t = f.read()
        names = ast.literal_eval(re.search(r'(?m)^LEDGER_READ = (\(.*\))$', t).group(1))
        filt = re.compile(ast.literal_eval(re.search(r'(?m)^SHELL_FILTER = re\.compile\((r\'.*\')\)$', t).group(1)))
        quoted = re.compile(ast.literal_eval(re.search(r'(?m)^QUOTED = re\.compile\((r\'.*\')\)$', t).group(1)))
        block = t.split("if name == 'G-RULE-POSTSEAL-READ':", 1)[1].split('if name == ', 1)[0]
        return names, re.findall(r"'([^']+)' not in c\['cmd'\]", block), filt, quoted
    except (OSError, ValueError, SyntaxError, AttributeError, IndexError):
        return None


def postseal_read(cmd, relay=RELAY):
    """v1.13.0: the command the arm would count: it names a ledger, carries none of the exclude list, and runs a shell filter outside quotes."""
    rule = ledger_rule(relay)
    if rule is None:
        return False
    names, excl, filt, quoted = rule
    return any(x in cmd for x in names) and not any(x in cmd for x in excl) and bool(filt.search(quoted.sub('""', cmd)))


def _gitwrite():
    """standing.gitwrite, its writes() the suite's own reading (tools/rule_arms.py GIT_WRITE); None where it does not import."""
    try:
        d = os.path.dirname(os.path.abspath(__file__))
        for p_ in (d, os.path.dirname(d)):
            if p_ not in sys.path:
                sys.path.insert(0, p_)
        import gitwrite as GW
        return GW
    except Exception:  # noqa: BLE001
        return None


def message_calls(transcript, tool_use_id=None, inp=None):
    """v1.17.0: the shell calls of the assistant message carrying this call, in their order, and this call's index among them: ([cmd], index);
    ([], None) where the transcript does not show it. Claude Code writes each block of a message as its own line under one message id, every
    block before any tool runs, so a parallel call's siblings stand in the transcript when the hook reads it."""
    try:
        with open(transcript, 'rb') as f:
            f.seek(0, 2)
            size = f.tell()
            f.seek(max(0, size - TAIL_BYTES))
            raw = f.read().decode('utf-8', errors='replace').split('\n')
    except (OSError, TypeError):
        return [], None
    blocks = []
    for l in raw:
        if '"tool_use"' not in l:
            continue
        try:
            j = json.loads(l)
        except ValueError:
            continue
        if j.get('type') != 'assistant':
            continue
        m = j.get('message') or {}
        for b in m.get('content') or []:
            if isinstance(b, dict) and b.get('type') == 'tool_use':
                blocks.append((m.get('id'), b.get('id'), b.get('name'), b.get('input') or {}))
    mine = None
    for k in range(len(blocks) - 1, -1, -1):
        _mid, bid, name, binp = blocks[k]
        if (tool_use_id and bid == tool_use_id) or (not tool_use_id and inp is not None and binp == inp):
            mine = k
            break
    if mine is None:
        return [], None
    mid = blocks[mine][0]
    same = [(i, b) for i, b in enumerate(blocks) if b[0] == mid and b[2] in ('Bash', 'PowerShell')]
    cmds = [b[3].get('command') or '' for _i, b in same]
    idx = next((n for n, (i, _b) in enumerate(same) if i == mine), None)
    return cmds, idx


def over_one_write(cmds, idx, GW=None):
    """v1.17.0, (R347)(2)(ii): this call's git writes and those of the calls before it in its message; True where this call carries one and
    the sum passes one. The first write of a message stands; the second, in a parallel call or chained in the same command, is refused."""
    GW = GW or _gitwrite()
    if GW is None or idx is None:
        return False
    mine = len(GW.writes(cmds[idx]))
    before = sum(len(GW.writes(c)) for c in cmds[:idx])
    return mine > 0 and before + mine > 1


def last_request(transcript):
    """v1.19.0, (R349)(2)(i): the stamp of the transcript's last api-request line, the message the next tool calls belong to; None where
    unread. Claude Code writes a message's api-request line before the message's tools run, and the message's own blocks after them
    (b738's 23:22:55Z pair: both blocks written after the second tool's result; b739's two probes: the first found neither block)."""
    try:
        with open(transcript, 'rb') as f:
            f.seek(0, 2)
            size = f.tell()
            f.seek(max(0, size - TAIL_BYTES))
            raw = f.read().decode('utf-8', errors='replace').split('\n')
    except (OSError, TypeError):
        return None
    for l in reversed(raw):
        if '"api-request"' not in l:
            continue
        try:
            j = json.loads(l)
        except ValueError:
            continue
        if j.get('type') == 'api-request':
            return j.get('timestamp') or None
    return None


def ledger_path(transcript):
    return os.path.join(tempfile.gettempdir(), 'standing-gitwrite-%s.json' % hashlib.sha256(str(transcript).encode('utf-8')).hexdigest()[:16])


def ledger_over(transcript, n, path=None):
    """v1.19.0, (R349)(2)(i): True where this call's n git writes follow a write already allowed in the same message, the message read as
    the transcript's last api-request; an allowed write is recorded in the ledger (path, or the session's file in the temporary directory)."""
    if n <= 0:
        return False
    key = last_request(transcript)
    if key is None:
        return False
    p = path or ledger_path(transcript)
    try:
        with open(p, encoding='utf-8') as f:
            j = json.load(f)
    except (OSError, ValueError):
        j = {}
    had = int(j.get('writes') or 0) if j.get('request') == key else 0
    if had >= 1:
        return True
    try:
        with open(p, 'w', encoding='utf-8', newline='\n') as f:
            json.dump(dict(request=key, writes=had + n), f)
    except OSError:
        pass
    return False


def subject_faults(cmd, relay=RELAY):
    """v1.19.0, (R349)(2)(iii): a seal or lock commit's subject read by tools/standing/subjects.py check() against the relay's banks; [] where
    the command carries no such subject. v1.21.0, (R351)(2)(i), b740 events (1): a gate, lock or seal commit typed into a shell is refused
    whatever its subject -- the shell stands between the subject and the commit (PowerShell's backtick); tools/standing/commit.py is the one route."""
    m = COMMIT_SUBJECT.search(cmd)
    if not m:
        return []
    subj = m.group(1) if m.group(1) is not None else m.group(2)
    s = re.match(r'^(b\d+) (seal|lock|gate):', subj)
    if not s:
        return step_subject_faults(subj, relay)
    return _seal_lock_faults(s, subj, relay)


def step_subject_faults(subj, relay=RELAY):
    """v1.25.0, (R355)(2)(v), b744 events (5): a step-row commit's subject ("bNNN <phase>: the step row(s) for ...") read against the rows the
    staged step bank adds over HEAD's (tools/standing/subjects.py step_rows_check); [] for any other subject."""
    d = os.path.dirname(os.path.abspath(__file__))
    if d not in sys.path:
        sys.path.insert(0, d)
    import subjects as SJ
    sm = SJ.STEP_SUBJECT.match(subj or '')
    if not sm:
        return []
    import subprocess
    rel = 'data/%s_steps.json' % sm.group(1)

    def g(ref):
        r = subprocess.run(['git', '-C', relay, 'show', '%s:%s' % (ref, rel)], capture_output=True)
        t = r.stdout.decode('utf-8', 'replace') if r.returncode == 0 else ''
        return json.loads(t) if t.strip() else {}
    return SJ.step_rows_check(subj, SJ.step_rows_added(g('HEAD'), g('')))


ROWID_COMMIT = re.compile(r'(?:\bcd\s+(?:"([^"]+)"|(\S+))\s*&&\s*)?\bgit\s+(?:-C\s+(?:"([^"]+)"|(\S+))\s+)*commit\b')


def rowid_faults(cmd, ctx=None):
    """v1.25.0, (R355)(2)(i), b743's [B1]-[B3]: a commit in PLACE-papers whose staged ledger files add a row whose ID the file already holds
    (tools/standing/rowid.py staged_refusals); the repository read from the command's -C or cd, else the hook input's cwd; [] otherwise."""
    m = ROWID_COMMIT.search(cmd or '')
    if not m:
        return []
    path = next((x for x in (m.group(3), m.group(4), m.group(1), m.group(2)) if x), None) or ((ctx or {}).get('cwd') or '')
    norm = path.replace('\\', '/').rstrip('/')
    if not norm.lower().endswith('place-papers'):
        return []
    repo = re.sub(r'^/([a-zA-Z])/', lambda k: k.group(1).upper() + ':/', norm)
    d = os.path.dirname(os.path.abspath(__file__))
    if d not in sys.path:
        sys.path.insert(0, d)
    import rowid as RI
    return ['%s :%d %s -- %s' % r for r in RI.staged_refusals(repo)]


def _seal_lock_faults(s, subj, relay=RELAY):
    if s.group(2) == 'gate':
        return ['a gate commit by the shell: tools/standing/commit.py makes it, its subject and its row']
    d = os.path.dirname(os.path.abspath(__file__))
    if d not in sys.path:
        sys.path.insert(0, d)
    import subjects as SJ

    def read(name):
        p = os.path.join(relay, 'data', name)
        if not os.path.exists(p):
            return None
        with open(p, encoding='utf-8') as f:
            return json.load(f) if name.endswith('.json') else f.read()
    return SJ.check(s.group(1), s.group(2), subj, read) + ['a %s commit by the shell: tools/standing/commit.py makes it, its subject and its row' % s.group(2)]


def locked(relay=RELAY):
    """v1.17.0: the open act's lock recorded (data/<act>_lockgate.json) and its closing not written."""
    act = bank_act(relay)
    return bool(act) and os.path.exists(os.path.join(relay, 'data', '%s_lockgate.json' % act)) and not os.path.exists(os.path.join(relay, 'data', '%s_closing.txt' % act))


def lock_exempt(act):
    """the banks written after the lock by design (standing.act.post_lock_appended) and the events bank, appended by the Edit tool after the lock."""
    try:
        import act as A_
        base = tuple(A_.post_lock_appended(act))
    except Exception:  # noqa: BLE001
        base = ('data/%s_steps.json' % act, 'data/%s_bank_hashes.json' % act, 'data/%s_hook_refusals.txt' % act, 'data/%s_address_scan_postlock.txt' % act, 'tools/mirror_prevbuild.json')
    return base + ('data/%s_events.txt' % act, 'data/%s_face_branches.json' % act)   # ### v1.24.0, (R354)(2)(v): the face's branch list, appended by its tool


def locked_bank(path, relay=RELAY, act=None):
    """v1.17.0, (R347)(2)(iii), b736 events (3): the path is one of the act's banks or tools, tracked at the relay, and not exempt: a write to it
    after the lock is refused before it lands. A file the lock never saw (untracked) is a new bank and passes."""
    act = act or bank_act(relay)
    if not act or not path:
        return False
    try:
        rel = os.path.relpath(os.path.abspath(path), relay).replace(os.sep, '/')
    except ValueError:
        return False
    # ### v1.24.0, (R354)(2)(iii), b743 events (4): the refusal binds banks and faces; the act module's post-lock edit is allowed, committed by
    # ### commit.py's repair phase under its three conditions and scored N4 REFUTED (the N4 route reads every post-lock tool edit), so an act can always seal
    ours = rel.startswith(('data/%s_' % act, 'tools/%s_' % act))
    if not ours or rel in lock_exempt(act):
        return False
    import subprocess
    r = subprocess.run(['git', '-C', relay, 'ls-files', '--error-unmatch', '--', rel], capture_output=True, text=True)
    return r.returncode == 0


def hashed_bank(path, relay=RELAY, act=None):
    """v1.21.0, (R351)(2)(ii), b740 (m), N4: the bank's name where the path is a file of relay data/ that the act's hashes bank names (a bank its tool
    wrote and hashed), else None. b740's data/b740_corrigendum.json, written by the c1 route and set by hand before the commit, is the instance; the
    lock never entered it (Component 1), so the LOCKED rule of v1.17.0 could not reach it. The exclusion of (R343)(2)(vi) is read through lock_exempt:
    the step bank, the hashes bank itself, the refusals, the post-lock scan and the events bank stay writable by their routes."""
    act = act or bank_act(relay)
    if not act or not path:
        return None
    try:
        rel = os.path.relpath(os.path.abspath(path), relay).replace(os.sep, '/')
    except ValueError:
        return None
    if not rel.startswith('data/') or '/' in rel[5:] or rel in lock_exempt(act):
        return None
    try:
        with open(os.path.join(relay, 'data', '%s_bank_hashes.json' % act), encoding='utf-8') as f:
            names = json.load(f)
    except (OSError, ValueError):
        return None
    return rel[5:] if isinstance(names, dict) and rel[5:] in names else None


def refusals_path(relay=RELAY):
    act = bank_act(relay)
    return os.path.join(relay, 'data', '%s_%s.txt' % (act, EXCLUDED_KIND) if act else 'act_unread_%s.txt' % EXCLUDED_KIND)


def strip_quotes(cmd):
    """The command with every quoted span replaced by a blank, quotes kept as markers."""
    out = []
    i, n = 0, len(cmd)
    while i < n:
        if cmd.startswith("@'", i) or cmd.startswith('@"', i):
            q = cmd[i + 1]
            end = cmd.find('\n' + q + '@', i + 2)
            if end < 0:
                return ''.join(out) + ' QQ', False
            out.append(' QQ ')
            i = end + 3
            continue
        c = cmd[i]
        if c == "'":
            end = cmd.find("'", i + 1)
            if end < 0:
                return ''.join(out) + ' QQ', False
            out.append(' QQ ')
            i = end + 1
            continue
        if c == '"':
            j = i + 1
            while j < n and cmd[j] != '"':
                j += 2 if cmd[j] in '\\`' else 1
            if j >= n:
                return ''.join(out) + ' QQ', False
            out.append(' QQ ')
            i = j + 1
            continue
        if c in '\\`' and i + 1 < n:
            out.append('  ')
            i += 2
            continue
        out.append(c)
        i += 1
    return ''.join(out), True


REDIR_CMDLET = re.compile(r'(?i)(?<![\w-])(?:Out-File|Set-Content|Add-Content|Tee-Object)(?![\w-])')
INNER_SHELL = re.compile(r"""(?i)(?<![\w./-])(?:bash|sh|powershell(?:\.exe)?|pwsh(?:\.exe)?|cmd(?:\.exe)?)(?:\s+-\w+)*\s+(?:-c|-Command|/c)\s+(?:'([^']*)'|"((?:[^"\\`]|[\\`].)*)")""", re.S)


def inner_shell_args(cmd):
    """the quoted arguments an inner shell runs: `bash -c '...'`, `sh -c "..."`, `powershell -Command "..."`, `cmd /c "..."`."""
    return [m.group(1) if m.group(1) is not None else m.group(2) for m in INNER_SHELL.finditer(cmd)]


def lines_of(path):
    """v1.4.0: the file's line count (its line feeds, and a last line without one), or None where it is not a readable file."""
    try:
        with open(path, 'rb') as f:
            b = f.read()
    except OSError:
        return None
    return b.count(b'\n') + (1 if b and not b.endswith(b'\n') else 0)


def judge(tool, inp, relay=RELAY, ctx=None):
    """(kind, detail) for a refusal, or None for an allowed call. v1.17.0: `ctx` the hook's whole input (its transcript_path and tool_use_id)."""
    if tool in EDIT_TOOLS:
        if locked(relay) and locked_bank(inp.get('file_path') or inp.get('notebook_path') or '', relay):
            return 'LOCKED', 'a %s of a bank written before the lock, after the lock' % tool
        hb = hashed_bank(inp.get('file_path') or inp.get('notebook_path') or '', relay)
        if hb:   # ### v1.21.0, (R351)(2)(ii), b740 (m)
            return 'HASHED', 'a %s of data/%s, a bank its tool wrote (data/%s_bank_hashes.json), by hand' % (tool, hb, bank_act(relay))
        return None
    if tool == 'Read':
        lim = inp.get('limit')
        if lim is None:
            return 'READ', 'a Read call with no limit'
        try:
            if int(lim) > LIMIT:
                return 'READ', 'a Read call with limit %s, above %d' % (lim, LIMIT)
        except (TypeError, ValueError):
            return 'READ', 'a Read call with an unreadable limit %r' % (lim,)
        # ### v1.4.0, (R334)(2)(ii): row (19)'s "by offset and a limit" on a file of two hundred lines or more -- a limit with no offset
        # ### on such a file is refused (the class the record tool's reads route counted after the fact, b721 (y), b722 (y), b723 (b'))
        if inp.get('offset') is None:
            n = lines_of(inp.get('file_path') or '')
            if n is not None and n >= LIMIT:
                return 'READ', 'a Read call with a limit and no offset on a file of %d lines' % n
        return None
    if tool in ('Bash', 'PowerShell'):
        cmd = inp.get('command') or ''
        bare, _closed = strip_quotes(cmd)
        if '|' in bare:
            return 'PIPE', 'a %s command carrying a pipe outside quotes' % tool
        if '>' in bare or '<' in bare:
            return 'REDIR', 'a %s command carrying a redirect outside quotes' % tool
        if REDIR_CMDLET.search(bare):   # ### v1.9.0, (R339)(2)(i): a redirect that carries no `>`
            return 'REDIR', 'a %s command carrying a redirect by cmdlet' % tool
        if INPLACE.search(bare):   # ### v1.18.0, (R348)(2)(iii), b737 (u): an in-place edit by the shell, the render re-run instead
            return 'INPLACE', 'a %s command editing a file in place (%s)' % (tool, INPLACE.search(bare).group(0).strip()[:60])
        if SED.search(bare):   # ### v1.19.0, (R349)(2)(vi), b738 (p): sed in any form, b685 rules row (2)
            return 'SED', 'a %s command running sed' % tool
        if inp.get('run_in_background') and (SUITE_PART.search(bare) or SUITE_COMBINE.search(bare)):   # ### v1.19.0, (R349)(2)(v), b738 events (6)
            return 'BACKGROUND', 'a suite part or combine sent to the background'
        for inner in inner_shell_args(cmd):   # ### v1.9.0, (R339)(2)(i): strip_quotes blanks an inner shell's argument, the one place a redirect passed the test above
            ibare, _c = strip_quotes(inner)
            if '|' in ibare or '>' in ibare or '<' in ibare:
                return 'REDIR', 'a %s command carrying a redirect or a pipe inside an inner shell`s quoted argument' % tool
        if bare.count('ls-remote') > 1:   # ### v1.8.0, (R338)(2)(iv)(d): b727 event (7), four reads chained in one diagnostic
            return 'REMOTE', 'a %s command carrying more than one remote read' % tool
        if len(SUITE_PART.findall(bare)) + len(SUITE_COMBINE.findall(bare)) > 1:   # ### v1.11.0: a chained suite call stands in the capture for good
            return 'SUITE', 'a %s command carrying more than one suite part or combine' % tool
        if BRANCH_DEL.search(bare) and not citation_done(relay):   # ### v1.11.0: the arm's clause, enforced before the delete and not read after it
            return 'ORDER', 'a branch delete before the act`s citation check'
        if sealed(relay) and postseal_read(cmd, relay):   # ### v1.13.0, (R343)(2)(vi): b732 event (11), two reads the arm found after they ran
            return 'POSTSEAL', 'a %s command running a shell filter over the entry or the trail after the seal' % tool
        for seg in re.split(r'&&|;|\n', bare):
            if ASSIGN.match(seg) or PS_ENV.match(seg):
                return 'ENV', 'a %s command prefixed by an environment-variable assignment' % tool
        GW = _gitwrite()
        if GW is not None and len(GW.writes(cmd)) > 1:   # ### v1.17.0, (R347)(2)(ii): add and commit chained count two
            return 'GITWRITE', 'a %s command carrying %d git writes' % (tool, len(GW.writes(cmd)))
        sf = subject_faults(cmd, relay)
        if sf:   # ### v1.19.0, (R349)(2)(iii), b738 events (4); v1.25.0, (R355)(2)(v): the step-row subject too
            return 'SUBJECT', 'a seal, lock or step-row commit whose subject differs from its bank: %s' % '; '.join(sf)[:200]
        try:
            rf = rowid_faults(cmd, ctx)
        except Exception as e:   # ### the reader's own failure refuses nothing silently: printed as the refusal's detail
            rf = ['the ID reader failed (%s)' % e]
        if rf:   # ### v1.25.0, (R355)(2)(i), b743's [B1]-[B3]
            return 'ROWID', 'a PLACE-papers commit adding a ledger row whose ID the file already holds: %s' % '; '.join(rf)[:200]
        if ctx and GW is not None:
            cmds, idx = message_calls(ctx.get('transcript_path'), ctx.get('tool_use_id'), inp)
            if over_one_write(cmds, idx, GW):
                return 'GITWRITE', 'a second git write in one message, across its parallel calls'
            if ledger_over(ctx.get('transcript_path'), len(GW.writes(cmd)), ctx.get('ledger')):   # ### v1.19.0, (R349)(2)(i), b738 (m)
                return 'GITWRITE', 'a second git write in one message, read by the message`s API request'
        return None
    return None


def refuse(kind, detail, tool, inp, relay=RELAY):
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    shown = inp.get('command') if tool != 'Read' else inp.get('file_path')
    reason = 'REFUSED %s: %s. ROW ENFORCED: %s' % (kind, detail, ROWS[kind])
    try:
        with open(refusals_path(relay), 'a', encoding='utf-8', newline='\n') as f:
            f.write('%s | %s | %s | %s | %s\n' % (stamp, kind, tool, json.dumps(shown, ensure_ascii=False)[:300],
                                                   detail))
    except OSError:
        pass
    return reason


def hook():
    try:
        data = json.load(sys.stdin)
    except ValueError as e:
        print('standing hook: unreadable hook input: %s' % e, file=sys.stderr)
        sys.exit(2)
    tool = data.get('tool_name', '')
    inp = data.get('tool_input') or {}
    try:
        verdict = judge(tool, inp, ctx=data)
    except Exception:  # noqa: BLE001  ### v1.17.0: a fault in the message read is no refusal; the suite's arms stand behind the hook
        verdict = judge(tool, inp)
    if verdict is None:
        sys.exit(0)
    reason = refuse(verdict[0], verdict[1], tool, inp)
    print(json.dumps({'hookSpecificOutput': {'hookEventName': 'PreToolUse', 'permissionDecision': 'deny',
                                             'permissionDecisionReason': reason}}, ensure_ascii=False))
    sys.exit(0)


def cases(act):
    ferry = 'D:/relay/data/%s_ferry.txt' % act
    return [
        ('Read', {'file_path': ferry}, 'READ'),
        ('Read', {'file_path': ferry, 'offset': 1, 'limit': 201}, 'READ'),
        ('Read', {'file_path': ferry, 'offset': 1, 'limit': 200}, None),
        ('Read', {'file_path': os.path.join(RELAY, 'tools', 'standing', 'hook.py'), 'limit': 60}, 'READ'),   # ### v1.4.0, (2)(ii)
        ('Read', {'file_path': os.path.join(RELAY, 'tools', 'standing', 'hook.py'), 'offset': 1, 'limit': 60}, None),
        ('Bash', {'command': 'git status | head'}, 'PIPE'),
        ('Bash', {'command': 'git log --oneline -3 2>&1'}, 'REDIR'),
        ('Bash', {'command': 'cat a > b'}, 'REDIR'),
        ('Bash', {'command': 'PYTHONIOENCODING=utf-8 python x.py'}, 'ENV'),
        ('Bash', {'command': 'cd /d/relay && FOO=1 python x.py'}, 'ENV'),
        ('Bash', {'command': 'cd /d/relay && python -I -X utf8 tools/locate.py data/x.txt "a|b>c"'}, None),
        ('Bash', {'command': 'git -C /d/relay commit -m "%s: a -> b, x|y"' % act}, None),
        ('Bash', {'command': 'git -C /d/a ls-remote origin ; git -C /d/b ls-remote origin'}, 'REMOTE'),   # ### v1.8.0, (2)(iv)(d)
        ('Bash', {'command': 'git -C /d/a ls-remote origin'}, None),
        ('Bash', {'command': 'python -X utf8 -u tools/standing/fold.py checks --combine x.txt && python -X utf8 -u tools/standing/fold.py checks --prev --part act'}, 'SUITE'),   # ### v1.11.0
        ('Bash', {'command': 'python -X utf8 -u tools/standing/fold.py checks --prev --part act'}, None),
        ('PowerShell', {'command': 'Get-ChildItem D:/relay | Select-Object -First 3'}, 'PIPE'),
        ('PowerShell', {'command': 'git status > out.txt'}, 'REDIR'),
        ('PowerShell', {'command': '$env:PYTHONIOENCODING = "utf-8"; python x.py'}, 'ENV'),
        ('PowerShell', {'command': "git commit -m @'\nline | with > marks\n'@"}, None),
        ('PowerShell', {'command': 'Get-PSDrive'}, None),
        ('PowerShell', {'command': 'git status > $null'}, 'REDIR'),   # ### v1.9.0, (R339)(2)(i), the two forms the ruling names
        ('Bash', {'command': 'python x.py 2>&1'}, 'REDIR'),
        ('Bash', {'command': "bash -c 'git status > out.txt'"}, 'REDIR'),   # ### the forms that did pass before this version
        ('Bash', {'command': 'sh -c "ls | wc -l"'}, 'REDIR'),
        ('PowerShell', {'command': 'powershell -Command "git log 2>&1"'}, 'REDIR'),
        ('PowerShell', {'command': 'git status; Set-Content -Path a -Value b'}, 'REDIR'),
        ('Bash', {'command': "bash -c 'git status'"}, None),
        ('Bash', {'command': 'git -C /d/relay commit -m "the Out-File rule"'}, None),
        ('Grep', {'pattern': 'a|b'}, None),
    ]


def sha256(p):
    with open(p, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def instance_record(prev):
    """(4)(iii)'s instance from the record: the previous act's hook bank, read against the sha256 its act's root names."""
    root = os.path.join(RELAY, 'data', '%s_act_root.json' % prev)
    rel = 'data/%s_%s.txt' % (prev, EXCLUDED_KIND)
    try:
        rj = json.load(open(root, encoding='utf-8'))
    except (OSError, ValueError):
        return dict(named=False, rel=rel, root=root)
    banks = dict(rj.get('banks') or {})   # a root's banks: its `banks` map, or its `items` rows "data/<name> <sha256>"
    for it in rj.get('items') or []:
        parts = it.split(' ')
        if len(parts) == 2 and parts[0].startswith('data/'):
            banks.setdefault(parts[0], parts[1])
    p = os.path.join(RELAY, *rel.split('/'))
    return dict(named=rel in banks, rel=rel, root=root, rooted=banks.get(rel), now=sha256(p) if os.path.isfile(p) else None)


def instance_constructed(act):
    """(4)(iii)'s constructed instance, in a scratch directory outside data/ and tools/: a test relay holding act_current.json, three
    banks and a test root naming them by sha256; one refusal sent through refuse() with the standing path, then one through a refuse
    bound to a rooted bank (the old form). Returns each run's changed root-named banks. Nothing is deleted; the scratch stays."""
    scratch = tempfile.mkdtemp(prefix='standing-hook-control-')
    d = os.path.join(scratch, 'data')
    os.makedirs(d)
    with open(os.path.join(d, 'act_current.json'), 'w', encoding='utf-8', newline='\n') as f:
        f.write(json.dumps({'act': act}) + '\n')
    named = ['%s_closing.txt' % act, '%s_defects.txt' % act, '%s_old_hook_bank.txt' % act]
    for n in named:
        with open(os.path.join(d, n), 'w', encoding='utf-8', newline='\n') as f:
            f.write('a test bank %s\n' % n)
    test_root = {'data/' + n: sha256(os.path.join(d, n)) for n in named}

    def changed():
        return sorted(r for r, h in test_root.items() if sha256(os.path.join(scratch, *r.split('/'))) != h)

    refuse('PIPE', 'the control`s refused call', 'Bash', {'command': 'git status | head'}, relay=scratch)
    new = changed()
    out = refusals_path(scratch)
    old_path = os.path.join(d, named[2])
    with open(old_path, 'a', encoding='utf-8', newline='\n') as f:   # the old form: the refusal appended to a bank the root names
        f.write('a refusal line, the old form\n')
    old = changed()
    return dict(scratch=scratch, new_changed=new, new_bank=os.path.relpath(out, scratch).replace(os.sep, '/'),
                new_bank_named='data/' + os.path.basename(out) in test_root, old_changed=old)


def control():
    act = act_of()
    prev = None
    try:
        prev = json.load(open(os.path.join(RELAY, 'data', 'act_current.json'), encoding='utf-8')).get('prev')
    except (OSError, ValueError):
        pass
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    lines = ['%s STANDING HOOK CONTROL -- v5 row (77) and the class repair (4)(iii), tools/standing/hook.py at %s' % (act, stamp),
             '### each case: tool | input | wanted | got | AS WANTED']
    ok = 0
    cs = cases(act)
    for tool, inp, want in cs:
        got = judge(tool, inp)
        got_kind = got[0] if got else None
        good = got_kind == want
        ok += good
        lines.append('%s | %s | %s | %s | %s' % (tool, json.dumps(inp, ensure_ascii=False), want or 'ALLOWED',
                                                 got_kind or 'ALLOWED', good))
    kinds = sorted({w for _t, _i, w in cs if w})
    lines.append('### ### **CASES %d ; AS WANTED %d ; REFUSAL KINDS %s ; ALLOWED CASES %d ; ALL AS WANTED %s**'
                 % (len(cs), ok, ','.join(kinds), sum(1 for c in cs if c[2] is None), ok == len(cs)))
    rec = instance_record(prev)
    con = instance_constructed(act)
    rec_class = bool(rec.get('named')) and rec.get('rooted') is not None and rec.get('now') != rec.get('rooted')
    con_ok = con['new_changed'] == [] and not con['new_bank_named'] and con['old_changed'] != []
    lines += ['', '### (4)(iii) INSTANCE 1, FROM THE RECORD: %s, named by %s: %s ; its sha256 at the root %s ; now %s ; the class (a refusal '
              'after the root changed a rooted bank) %s' % (rec['rel'], os.path.basename(rec['root']), rec.get('named'),
                                                            (rec.get('rooted') or '-')[:16], (rec.get('now') or '-')[:16],
                                                            'SHOWN' if rec_class else 'NOT SHOWN'),
              '### (4)(iii) INSTANCE 2, CONSTRUCTED in %s: the standing refuse() wrote %s (named by the test root %s) and changed root-named '
              'banks %s ; the old form (the refusal appended to a root-named bank) changed %s ; AS WANTED %s' % (
                  con['scratch'], con['new_bank'], con['new_bank_named'], con['new_changed'] or 'none', con['old_changed'] or 'none', con_ok),
              '### ### **(4)(iii) CONTROL: THE RECORD`S INSTANCE %s ; THE CONSTRUCTED %s ; THE REPAIR HOLDS %s.**' % (
                  'SHOWN' if rec_class else 'NOT SHOWN', 'AS WANTED' if con_ok else 'NOT AS WANTED', rec_class and con_ok and ok == len(cs))]
    bank = os.path.join(RELAY, 'data', '%s_hook_control.txt' % act)
    with open(bank + '.tmp', 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(lines) + '\n')
    os.replace(bank + '.tmp', bank)
    print('\n'.join(lines[-4:]))
    print('bank', bank)


def excludes():
    """v1.17.0, (R347)(2)(vi), b736 events (8): the post-seal read rule printed before any read after the seal, as the arm holds it (tools/rule_arms.py):
    the ledger names, the exclude list, and the one route allowed (the Read tool)."""
    rule = ledger_rule()
    if rule is None:
        print('### THE POST-SEAL RULE NOT READ from tools/rule_arms.py')
        return 1
    names, excl, _f, _q = rule
    print('### THE POST-SEAL READ RULE (G-RULE-POSTSEAL-READ, tools/rule_arms.py): after the seal no shell filter or redirect over %s ; the commands it excludes, by their text: %s ; the entry and the trail read by the Read tool alone'
          % (', '.join(names), ', '.join(excl) or 'none'))
    return 0


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'excludes':
        sys.exit(excludes())
    if len(sys.argv) > 1 and sys.argv[1] == 'control':
        control()
    else:
        hook()
